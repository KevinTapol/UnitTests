# Vitest
<!-- 10:55 -->
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

***tsconfig.json file does not currently exist***

*To set up typescript type error for import.meta.vitest go to tsconfig.json and add* 
"types": [
    "vitest/importMeta"
]

*To allow inline testing on the same file, go to vite.config.ts and add the following inside the test object*
includeSource: ["src/**/*,{js,ts}"],
