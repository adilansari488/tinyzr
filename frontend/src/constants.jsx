const baseURL = window.location.origin ;
let ENV ;
let apiURL ;
if (baseURL == "https://urlshortener.tinyzr.link") {
    ENV = "prod" ;
    apiURL = "https://tinyzr.link/url" ;
}
else {
    ENV = "dev"
    apiURL = "https://fiqbr34nj8.execute-api.ap-south-1.amazonaws.com/dev/url" ;
}

export default apiURL 