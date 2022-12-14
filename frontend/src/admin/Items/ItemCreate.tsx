import React, { FC } from 'react';
import { Create, SimpleForm, TextInput } from 'react-admin';

export const ItemCreate: FC = (props) => (
  <Create {...props}>
    <SimpleForm>
      <TextInput source="name" />
      <TextInput source="price" />
    </SimpleForm>
  </Create>
);
