# Vitest
The goal of this repo is to learn the Unit Testing Software Vitest designed for Vite.

<a target="_blank" href="https://www.youtube.com/watch?v=7f-71kYhK00&t=339s&ab_channel=WebDevSimplified">Click here for WebDevSimplified's tutorial on **Unit Testing with Vitest for Vite**</a>
*create a vite project with vanilla js using typescript*
 - npm create@latest .
 - select vanilla
 - select typescript

*install vitest as a dev dependency*
 - npm i --save-dev vitest

*in package.json add a test script for vitest*
"test": "vitest"

*if you want your test script to render the coverage data to include HTML then change the script to the following and select yes to install the dependency @vitest/coverage-v8*
 "test": "vitest --coverage"