import axios from 'axios';
import type {AxiosInstance} from 'axios';


const apiClient: AxiosInstance = axios.create({
  baseURL: "http://localhost:8080/",
  headers: {
    "Content-type": "application/json",
  },
});

class ApiService {
    getAll() {
        return apiClient.get("/data");
    }

    create(data: any) {
        return apiClient.post("/data", data);
    }

    update(id: any, data: any) {
        return apiClient.put(`/data/${id}`, data);
    }

    delete(id: any) {
        return apiClient.delete(`/data/${id}`);
    }

    deleteMany(ids: any) {
        return apiClient.post(`/data/deleteMany`, ids);
    }

    synchronize() {
        return apiClient.post(`/synchronize_live`);
    }
}

export default new ApiService();

