package main

import (
	"fmt"
	"os"
	"strconv"
)

func main() {
    input, err := os.ReadFile("./input")
    if err != nil {
        panic(err)
    }
    input_str := string(input)
    current_floor := 0
    for i := range input_str {
        if input_str[i] == '(' {
            current_floor++
        } else if input_str[i] == ')' {
            current_floor--
        } else if input_str[i] == '\n' {
            continue
        } else {
            panic(fmt.Sprintf("Invalid input character at %d: %q", i, input_str[i]))
        }
    }
    err = os.WriteFile("./a_output", []byte(strconv.Itoa(current_floor)), 0400)
    if err != nil {
        panic(err)
    }
}
