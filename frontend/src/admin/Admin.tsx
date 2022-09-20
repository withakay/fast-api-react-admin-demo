import React, { FC } from 'react';
import { fetchUtils, Admin as ReactAdmin, Resource, RouteWithoutLayout } from 'react-admin';
import { Route } from "react-router-dom";
import simpleRestProvider from 'ra-data-simple-rest';
import authProvider from './authProvider';
import { Login, SignUp } from '../views'

import { UserList, UserEdit, UserCreate } from './Users';
import { ItemList, ItemCreate, ItemShow, ItemEdit, ItemSummary } from './Items';

const httpClient = (url: any, options: any) => {
  if (!options) {
    options = {};
  }
  if (!options.headers) {
    options.headers = new Headers({ Accept: 'application/json' });
  }
  const token = localStorage.getItem('token');
  options.headers.set('Authorization', `Bearer ${token}`);
  return fetchUtils.fetchJson(url, options);
};

const dataProvider = simpleRestProvider('api/v1', httpClient);

const customRoutes = [
    <Route path="/item-summary">
        <ItemSummary/>
    </Route>,
    <RouteWithoutLayout path="/signup"  >
        <SignUp/>
    </RouteWithoutLayout>
]

export const Admin: FC = () => {
  return (
    <ReactAdmin dataProvider={dataProvider} authProvider={authProvider} customRoutes={customRoutes} loginPage={Login}>

      <Resource
        name="items"
        list={ItemList}
        edit={ItemEdit}
        create={ItemCreate}
        show={ItemShow}
      />

      <Resource
        name="users"
        list={UserList}
        edit={UserEdit}
        create={UserCreate}
      />

    </ReactAdmin>
  );
};
