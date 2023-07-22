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
    basement := 0
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
        if current_floor == -1 {
            basement = i + 1
            break
        }
    }
    err = os.WriteFile("./output_b", []byte(strconv.Itoa(basement)), 0400)
    if err != nil {
        panic(err)
    }
}
