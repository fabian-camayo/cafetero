import axios, { AxiosInstance } from "axios";
import store from '@/store/index';

const token = store.getters.token;
console.log(token);
const apiClient: AxiosInstance = axios.create({
  baseURL: "http://127.0.0.1:8000/api/v1/",
  headers: {
    "Authorization": "JWT "+token,
    "Content-type": "application/json",
  },
});

export default apiClient;