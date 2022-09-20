// in src/users.js
import React, { FC } from 'react';
import {
  List,
  Datagrid,
  TextField,
  BooleanField,
  EmailField,
  EditButton, Title,
} from 'react-admin';

import Button from '@material-ui/core/Button'
import Card from '@material-ui/core/Card'
import CardContent from '@material-ui/core/CardContent'

import { Link } from "react-router-dom";

export const ItemList: FC = (props) => (
    <>
      <List {...props}>
        <Datagrid rowClick="edit">
          <TextField source="id" />
          <TextField source="name" />
          <TextField source="price" />
          <EditButton />
        </Datagrid>
      </List>
        <Link to="item-summary" ><Button>Summary</Button></Link>
    </>
);
