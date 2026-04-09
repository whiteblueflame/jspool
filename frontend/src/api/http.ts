import axios from 'axios'

const baseURL =
  import.meta.env.VITE_API_BASE_URL && import.meta.env.VITE_API_BASE_URL.length > 0
    ? import.meta.env.VITE_API_BASE_URL
    : ''

const http = axios.create({
  baseURL,
  timeout: 30000,
})

export default http
