import React, {FC} from 'react';
import {
  Show,
  SimpleShowLayout,
  TextField
} from 'react-admin';

export const ItemShow: FC = (props) => (
  <Show {...props}>
    <SimpleShowLayout>
      <TextField source="id" />
      <TextField source="name" />
      <TextField source="price" />
    </SimpleShowLayout>
  </Show>
);
