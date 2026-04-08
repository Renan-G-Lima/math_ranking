export class connection_link{
    url = "http://127.0.0.1:5500";
    
    getUrl(route) {
        return this.url+route;
    }
}