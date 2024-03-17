# Jest Unit Tests

<a target="_blank" href="https://www.youtube.com/watch?v=FgnxcUQ5vho&t=622s&ab_channel=WebDevSimplified">Click here for WebDevSimplified's tutorial on **Unit Testing with Jest for JavaScript**</a>
 - npm init -y
 - npm i --save-dev jest
*change the following in package.json*
 - *before* "test": "echo \"Error: no test specified\" && exit 1" 
    *after* "test": "jest"
*if changed to "test": "jest --coverage" then it will create a coverage folder with an index.html file with tests*

*npm test* runs all jest .test.js
*npm test fileName* runs the specific *fileName*
