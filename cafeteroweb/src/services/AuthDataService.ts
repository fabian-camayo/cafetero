import http from "@/http-common";

/* eslint-disable */
class AuthDataService {

  create(data: any): Promise<any> {
    return http.post("/auth/access_token", data);
  }

}

export default new AuthDataService();