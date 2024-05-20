package main

import "fmt"

func fract(n int){
	if n == 1{
		fmt.Println("-");
		return
	} 
	fract(n - 1)
	for i := 0; i < n; i += 1{
		fmt.Printf("-")
	}
	fmt.Printf("\n")
	fract(n -1)
}

func main(){
	fract(100)	
}