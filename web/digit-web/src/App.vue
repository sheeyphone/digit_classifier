<script setup>
import {ref, onMounted} from 'vue'

let isDrawing = false
let keepDrawing = null
let lastX = 0
let lastY = 0
const onMousedown = e => {
  isDrawing = true
  if (!keepDrawing) {
    clearCanvas()
  }
  clearTimeout(keepDrawing)
  keepDrawing = null
  const {offsetX, offsetY} = e
  lastX = offsetX
  lastY = offsetY
}
const onMouseup = () => {
  if (isDrawing) {
    isDrawing = false
    keepDrawing = setTimeout(() => {
      keepDrawing = null
      sendToBackend()
    }, 500)
  }
}
const onMousemove = e => {
  if (isDrawing) {
    const {offsetX, offsetY} = e
    context.strokeStyle = 'white'
    context.lineWidth = 10
    context.lineJoin = 'round'
    context.lineCap = 'round'
    context.beginPath()
    context.moveTo(lastX, lastY)
    context.lineTo(offsetX, offsetY)
    context.stroke()
    lastX = offsetX
    lastY = offsetY
  }
}

let canvas, context
const initPaintBoard = () => {
  canvas = document.getElementById('PaintBoard')
  context = canvas.getContext('2d')
}
const clearCanvas = () => {
  context.fillStyle = 'black'
  context.fillRect(0, 0, canvas.width, canvas.height)
}

const classifyResult = ref('Unsolved')
const sendToBackend = () => {
  const imageDataURL = canvas.toDataURL()
  fetch('/digit', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({image: imageDataURL}),
  })
    .then(response => {
      if (response.ok) {
        return response.json()
      } else {
        console.error('Failed')
      }
    })
    .then(data => {
      classifyResult.value = data.result
    })
    .catch(error => {
      console.error('Error:', error)
    })
}

onMounted(() => {
  initPaintBoard()
})
</script>

<template>
  <div class="p-4 select-none flex flex-col space-y-6 w-[360px]">
    <div>
      <div class="text-3xl font-bold">Simple Digit Classifier</div>
      <div class="font-bold">Only single digit from 0 to 9</div>
    </div>
    <div class="h-[1px] bg-black/10"></div>
    <div class="flex flex-col space-y-2">
      <div>Drawing here:</div>
      <div class="flex h-[280px] w-[280px] items-center justify-center border-black-100 bg-black/5 rounded border">
        <canvas
          id="PaintBoard"
          class="bg-black"
          height="256"
          width="256"
          @mousedown="onMousedown"
          @mousemove="onMousemove"
          @mouseup="onMouseup"
          @mouseout="onMouseup"
        ></canvas>
      </div>
    </div>
    <div class="h-[1px] bg-black/10"></div>
    <div class="flex space-x-2 items-end">
      <span>Classify result is:</span>
      <span class="text-2xl font-bold">{{ classifyResult }}</span>
    </div>
  </div>
</template>

<style scoped></style>
