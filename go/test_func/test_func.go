package main

import (
	"fmt"
)

func main() {
	var a int = 3
	var b int = 4
	fmt.Printf("main, a=%d, b=%d\n", a, b)
	c := sum(a, b)
	fmt.Printf("main c=%d\n", c)
}

func sum(a, b int) int {
	fmt.Printf("sum, a=%d, b=%d\n", a, b)
	num := a + b
	return num
}
