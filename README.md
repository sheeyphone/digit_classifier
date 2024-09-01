# Digit classifier

This is a full-stack project from model training with `pytorch`, model saving as `hugging-face` model, back-end web service with `flask` and front-end web app with `vite.js` and `vue.js`!

We use a fairly simple dataset named MNIST. The MNIST database is a large database of handwritten digits that is commonly used for training various image processing systems. The database is also widely used for training and testing in the field of machine learning. [Wikipedia - MNIST database](https://en.wikipedia.org/wiki/MNIST_database)

## Project files introduction

| Folder or File       | use to                                |
| -------------------- | ------------------------------------- |
| model_training.ipynb | Train our model                       |
| model.py             | Model definition for back-end servide |
| app.py               | Flask back-end servide                |
| /web                 | Vue.js web-app with Vite.js           |
| /cache               | Temp folder to cache received_image   |

## Quick start

### 1. Checkout your dependencies

To make sure we could start this project, we need to install Python and Node.js with pnpm.

- Python env [Python3](https://www.python.org/)
- Node.js env [Node.js](https://nodejs.org/)
- pnpm [pnpm](https://pnpm.io/)
- Front-end env dependencies [Vite.js](https://vitejs.dev/)

### 2. Initialize the venv

> **_Run the commands below line by line._**

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

### 3. Train our model

Open `model_training.ipynb` and run all the cells. If you are skillful to edit it. That is awesome!
After running all cells, especially the saving cell, we could find a new folder named `model` in our project folder. You are right, that is our trained model. Out back-end service will serve with this model.

### 4. Start our back-end service

```bash
flask --app app.py run
```

### 5. Initialize the front-end

> **_Open another terminal and run the commands below line by line._**

```bash
cd web/digit-web
pnpm install
pnpm dev
```

You could see `VITE v5.4.2  ready in 191 ms`. Then open your browser with this address `http://localhost:5173` to see our WebApp, a simple drawing board to draw some digits.

> To here, congratulations, Bob is your uncle!

## Contributing

Thanks for the dataset from [ylecun/mnist](https://huggingface.co/datasets/ylecun/mnist).

If you have any questions about this project, please feel free to email me. ^^!
