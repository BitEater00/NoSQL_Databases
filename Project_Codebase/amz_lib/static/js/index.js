console.log("index.js linked");

/*
function getBookDetails() {
  //   let ASIN = "1623439671";
  const url = `https://www.googleapis.com/books/v1/volumes?q=${ASIN}`;

  fetch(url)
    .then((response) => {
      console.log(response);
      return response.text();
    })
    .then((data) => {
      retrieveData = JSON.parse(data);
      let author = retrieveData.items[0].volumeInfo.authors;
      let title = retrieveData.items[0].volumeInfo.title;
      // console.log(retrieveData.items);
      console.log(author);
      console.log(title);
    });
}
*/
// getBookDetails();
