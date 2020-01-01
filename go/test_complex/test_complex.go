package main

import (
	"fmt"
)

func main() {
	var a complex128 = complex(1, 2)
	var b complex128 = complex(3, 4)
	fmt.Println(a * b)
	fmt.Println(real(a))
	fmt.Println(imag(a))

}
