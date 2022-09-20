import React, { FC } from 'react';
import { Edit, SimpleForm, TextInput } from 'react-admin';

export const ItemEdit: FC = (props) => (
  <Edit {...props}>
    <SimpleForm>
      <TextInput disabled source="id" />
      <TextInput source="name" />
      <TextInput source="price" />
    </SimpleForm>
  </Edit>
);
