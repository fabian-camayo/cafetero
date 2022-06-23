import http from "@/http-common";
/* eslint-disable */
class BatchDataService {
  getAll(): Promise<any> {
    return http.get("/users");
  }

  get(id: any): Promise<any> {
    return http.get(`/users/${id}`);
  }

  create(data: any): Promise<any> {
    return http.post("/users", data);
  }

  update(id: any, data: any): Promise<any> {
    return http.put(`/update-user/${id}`, data);
  }

  delete(id: any): Promise<any> {
    return http.delete(`/update-user/${id}`);
  }

  deleteAll(): Promise<any> {
    return http.delete(`/update-user`);
  }

}

export default new BatchDataService();