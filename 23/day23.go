package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func main() {
	data, err := ioutil.ReadFile("input2.txt")
	if err != nil {
		fmt.Printf("%v+\n", err)
	}
	convertedData := prepareData(data)

	// channelSecond := make(chan string)

	resultFirst := quiz1(convertedData)
	// go quiz2(convertedData, channelSecond)

	// resultSecond := <-channelSecond
	fmt.Println("Ciao")
	fmt.Println(resultFirst)
	// fmt.Println(resultSecond)
}

func prepareData(data []byte) []int64 {
	stringedData := string(data)
	splitData := strings.Split(stringedData, "")
	intData := []int64{}
	for _, number := range splitData {
		converted, _ := strconv.ParseInt(number, 10, 64)
		intData = append(intData, converted)
	}
	return intData
}

func pickNumbers(selectedPos int, data []int64) []int64 {
	pick := []int64{}
	current := selectedPos + 1
	for i := 0; i < 3; i++ {
		pick = append(pick, data[(current+i)%len(data)])
	}
	return pick
}

func getDestination(element int64, pick []int64, length int64) int64 {
	destination := element
	found := false
	for {
		destination = ((destination + length - 2) % length) + 1
		found = getIndex(pick, element) != -1
		if !found {
			break
		}
	}
	return destination
}

func remove(slice []int64, element int64) []int64 {
	for i, item := range slice {
		if item == element {
			return append(slice[0:i], slice[i+1:]...)
		}
	}
	return slice
}

func elaborate(iterations int, data []int64) []int64 {

	selectedPos := 0
	maxNumber := getMax(data)
	for i := 0; i < iterations; i++ {
		pick := pickNumbers(selectedPos, data)
		selected := (data)[selectedPos]
		destination := getDestination(selected, pick, int64(len(data)))
		for _, number := range pick {
			data = remove(data, number)
		}
		destinationPos := getIndex(data, destination)
		suffix := (data)[destinationPos+1:]
		data = append((data)[0:destinationPos+1], pick...)
		data = append((data), suffix...)
		data = shift(selected, selectedPos, data)
		selectedPos = int(int64((selectedPos + 1)) % maxNumber)
	}
	return data
}

func getMax(slice []int64) int64 {
	max := int64(0)
	for _, item := range slice {
		if item > max {
			max = item
		}
	}
	return max
}

func shift(selected int64, selectedPos int, data []int64) []int64 {
	newSelectedPos := getIndex(data, selected)
	if newSelectedPos < selectedPos {
		data = append((data)[len((data))-(selectedPos-newSelectedPos):len(data)],
			(data)[0:len((data))-(selectedPos-newSelectedPos)]...)
	} else if newSelectedPos > selectedPos {
		data = append((data)[newSelectedPos-selectedPos:], (data)[0:newSelectedPos-selectedPos]...)
	}
	return data
}

func getIndex(slice []int64, element int64) int {
	for i, item := range slice {
		if item == element {
			return i
		}
	}
	return -1
}

func quiz1(data []int64) string {
	data = elaborate(100, data)
	result := ""
	current := getIndex(data, 1)
	for i := 0; i < len(data)-1; i++ {
		result += string(strconv.FormatInt(data[(current+i)%len(data)], 10))
	}
	return result
}

func quiz2(data []int64, c chan string) {

}
