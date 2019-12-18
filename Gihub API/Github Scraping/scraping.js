// const axios = require('axios')
// axios.get('http://jsonplaceholder.typicode.com/posts')
//   .then(response => {
//     console.log(response)
//   })
//   .catch(err => {
//     console.log(err)
//   })


var request = require("request");
// let ab
// ab = request({
//   url: "https://github.com/edugieun/Algorithm-Solving/blob/master/Array/0000_Bomber1(D3%2C%20Matrix)/bomber1.py",
// }, function(error, response, body) {
//   let start = 0
//   let end = 0
//   for (let i = 0; i < body.length; i++) {
//     if (body[i] === '<' && body[i+1] === 't' && body[i+2] === 'a' && body[i+3] === 'b' && body[i+4] === 'l') {
//       start = i
//     }
//     if (body[i] === '/' && body[i+1] === 't' && body[i+2] === 'a' && body[i+3] === 'b' && body[i+4] === 'l') {
//       end = i + 8
//       let table_ele = ''
//       for (i = start; i < end; i++) {
//         table_ele = table_ele + body[i]
//       }
//       return table_ele
//       // console.log(table_ele)
//       // break
//     }
//   }
// })
// console.log(ab)

// function getpage(link, callback){
//   var options = {
//   method: 'GET',
//   uri: link,
//   };
//   request(options, function (err, response, body) {
//      callback(body);
//   });
// }

// function getdata(data){
//   console.log(data)
// }

// // getpage("https://github.com/edugieun/Algorithm-Solving/blob/master/Array/0000_Bomber1(D3%2C%20Matrix)/bomber1.py", console.log)
// getpage("https://github.com/edugieun/Algorithm-Solving/blob/master/Array/0000_Bomber1(D3%2C%20Matrix)/bomber1.py", getdata)


function getpage(link, callback){
  request({
    url: link,
  }, function(error, response, body) {
    let start = 0
    let end = 0
    for (let i = 0; i < body.length; i++) {
      if (body[i] === '<' && body[i+1] === 't' && body[i+2] === 'a' && body[i+3] === 'b' && body[i+4] === 'l') {
        start = i
      }
      if (body[i] === '/' && body[i+1] === 't' && body[i+2] === 'a' && body[i+3] === 'b' && body[i+4] === 'l') {
        end = i + 8
        let table_ele = ''
        for (i = start; i < end; i++) {
          table_ele = table_ele + body[i]
        }
        callback(table_ele)
      }
    }
  })
}

function getdata(data){
  console.log(data)
}

getpage("https://github.com/edugieun/Algorithm-Solving/blob/master/Array/0000_Bomber1(D3%2C%20Matrix)/bomber1.py", getdata)