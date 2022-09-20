import { BACKEND_URL, ITEM_SUMMARY_URL } from '../config';
import { fetchUtils } from 'react-admin';

export const getMessage = async () => {
  const response = await fetch(BACKEND_URL);

  const data = await response.json();

  if (data.message) {
    return data.message;
  }

  return Promise.reject('Failed to get message from backend');
};

const httpClient = async (url: any, options: any = null) => {
  if (!options) {
    options = {};
  }
  if (!options.headers) {
    options.headers = new Headers({ Accept: 'application/json' });
  }
  const token = localStorage.getItem('token');
  options.headers.set('Authorization', `Bearer ${token}`);
  return await fetch(url, options);
};

export const getItemSummary = async () => {
  const response = await httpClient(ITEM_SUMMARY_URL);

  const data = await response.json();

  if (data.total) {
    return data.total;
  }

  return Promise.reject('Failed to get item summary from backend');
};
