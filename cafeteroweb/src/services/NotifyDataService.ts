import http from "@/http-common";
/* eslint-disable */
class NotifyDataService {
  send(data: any): Promise<any> {
    return http.post("/notify", data);
  }
}

export default new NotifyDataService();