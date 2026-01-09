# Image Color Quantization Using Elbow Method

## Goal

In this assignment, you will work with an image called `landscape.jpg`, located here: <a href="landscape.jpg">image</a>

<img src="landscape.jpg" />

Your task is to:

* Use the **Elbow Method** to determine the optimal number of clusters (k)
* Reduce the number of colors in the image according to the chosen k
* Apply the exact approach demonstrated in class

## Step 1: Finding the Optimal k (Elbow Method)

To decide how many clusters (color centers) should be used, apply the **Elbow Method** as learned in class.

The idea:

* Run clustering with different values of k
* Measure how the clustering error changes
* Choose the value of k where improvement starts to slow down (the "elbow")

<a href="Fb-kmean.md" >Link to class code – Elbow Method</a>

## Step 2: Image Color Quantization

After choosing the optimal k:

* Apply clustering to the image pixels
* Replace each pixel’s color with the color of its cluster center
* This reduces the image to k dominant colors

The result should be a visually simplified version of the original image, using only the selected number of colors

<a href="Fc-kmean-image.md">Link to class code – Image Processing & Color Reduction</a>

## Submission Email

**Send to:** [pythonai200425+knnfil@gmail.com](mailto:pythonai200425+knnfil@gmail.com)
