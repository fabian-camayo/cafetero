import http from "@/http-common";
/* eslint-disable */
class BatchDataService {
  getAll(): Promise<any> {
    return http.get("/batchs");
  }

  get(id: any): Promise<any> {
    return http.get(`/batchs/${id}`);
  }

  create(data: any): Promise<any> {
    return http.post("/batchs", data);
  }

  update(id: any, data: any): Promise<any> {
    return http.put(`/update-batch/${id}`, data);
  }

  delete(id: any): Promise<any> {
    return http.delete(`/update-batch/${id}`);
  }

  deleteAll(): Promise<any> {
    return http.delete(`/update-batch`);
  }

}

export default new BatchDataService();