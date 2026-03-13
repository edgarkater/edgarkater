package main

import (
	"fmt"
)

func add(a, b int) int {
	return a + b
}

func main() {
	var a, b int

	fmt.Println("Hello World")
	fmt.Print("Gib die erste Zahl ein: ")
	fmt.Scanln(&a)
	fmt.Print("Gib die zweite Zahl ein: ")
	fmt.Scanln(&b)

	summe := add(a, b)
	fmt.Println("Das Ergebnis lautet: ", summe)
}
