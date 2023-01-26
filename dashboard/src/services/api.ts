import type {AxiosInstance} from 'axios';
import axios from 'axios';


const apiClient: AxiosInstance = axios.create({
  baseURL: "http://localhost:5000/",
  headers: {
    "Content-type": "application/json",
  },
});

class ApiService {
    async getAll() {
        const promise = apiClient.get("/data")
        const response = promise.then((response) => {
            response.data
        })
        return response
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

