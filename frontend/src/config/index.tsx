export const BASE_URL: string = 'http://localhost:8000';
export let BACKEND_URL: string = 'http://example.com';
BACKEND_URL = !!process.env.REACT_APP_BACKEND_URL
  ? process.env.REACT_APP_BACKEND_URL
  : 'http://example.com';
export const ITEM_SUMMARY_URL: string = `${BACKEND_URL}/items/summary`;
