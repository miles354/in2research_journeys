---
title: Development of benchmarks in excalibur and measuring performance on HPC systems.
date: 2025-06-27
time: "15:30:00"
author: luthyanof
categories: ["learning", "OpenFOAM", "Spack", "motorBike CPU benchmark"] 
layout: post
---
___________________________________________________________________________________________________________________________________
**Introduction**
___________________________________________________________________________________________________________________________________

This week, I have focused on understanding what makes a good benchmark. One effective way to do this was by studying an existing
benchmark, such as the motorBike CPU benchmark in OpenFOAM. This has helped me learn how benchmarks are structured and how to
design them effectively in the future.

In addition, I have learned more about the CFD software called `OpenFOAM`, which can be used to run the motorBike CPU benchmark. 
This experience has given me a better understanding of what constitutes a benchmark.

___________________________________________________________________________________________________________________________________
**Challenges**
___________________________________________________________________________________________________________________________________

I encountered some challenges while analyzing the files within the motorBike CPU benchmark and running the test. Initially, I tried
to recreate files such as `control`, `mesh`, and `hexMesh` with little success. After some time, I realized that these files 
already existed and that you need to reference them to perform tasks like generating a mesh. Working through these difficulties has
helped me better understand the structure of benchmarks and steps involved in executing them.

After that, I researched how to visually represent the data collected after running the test, which led to the image below by using
`paraFoam`.

![Test1](/in2research_journeys/image/2025/06/Test1.png)
*Public domain from [Paraview in OpenFOAM]*

Finally, I explored the idea of using `paraFoam` within the processor files, which resulted in a temporary file where the visualized
result changed shape, as shown in the image below.

![Test2](/in2rearch_journeys/image/2025/06/Test2.png)
*Public domain from [Paraview in OpenFoam]*

___________________________________________________________________________________________________________________________________
**Stress Relief**
___________________________________________________________________________________________________________________________________

![Suprised Kitty](/in2research_journeys/images/2025/06/beautiful-grey-tabby-cat-with-yellow-eyes-stands-white-floor.jpg)
*Public domain from [Freepik](https://www.freepik.com/free-photo/beautiful-grey-tabby-cat-with-yellow-eyes-stands-white-floor_2612788.htm#fromView=keyword&page=1&position=0&uuid=8f3581b5-001f-4e2d-811a-d61654d0b1c2&query=Surprised+Cat)* 

