package main

import (
	"image"
	"image/color"
	"image/gif"
	"io"
	"math"
	"math/rand"
	"os"
	"time"
)

//var palette = []color.Color{color.White, color.Black}
var palette = []color.Color{color.RGBA{0x11, 0xFF, 0x55, 0x22},
	color.RGBA{0xFF, 0xAA, 0x11, 0x44}}

const (
	whiteIndex = 0 // palatte first color
	blackIndex = 1 // palatte second color
)

func main() {
	rand.Seed(time.Now().UTC().UnixNano())
	lissajous(os.Stdout)
}

func lissajous(out io.Writer) {
	const (
		cycles  = 5     // xが完了する周回回数
		res     = 0.001 // 回転の分解能
		size    = 100   // canvas size
		nframes = 64    // animation frams
		delay   = 1     // 10ms frame delay
	)
	freq := rand.Float64() * 3.0 // y の周波数
	anim := gif.GIF{LoopCount: nframes}
	phase := 0.0
	for i := 0; i < nframes; i++ {
		rect := image.Rect(0, 0, 2*size+1, 2*size+1)
		img := image.NewPaletted(rect, palette)
		for t := 0.0; t < cycles*2*math.Pi; t += res {
			x := math.Sin(t)
			y := math.Sin(t*freq + phase)
			img.SetColorIndex(size+int(x*size+0.5), size+int(y*size+0.5), blackIndex)
		}
		phase += 0.1
		anim.Delay = append(anim.Delay, delay)
		anim.Image = append(anim.Image, img)
	}
	gif.EncodeAll(out, &anim)
}
