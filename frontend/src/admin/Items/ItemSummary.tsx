import React, { FC, useState, useEffect } from 'react'
import Button from '@material-ui/core/Button'
import Card from '@material-ui/core/Card'
import CardContent from '@material-ui/core/CardContent'
import { Title } from 'react-admin'

import { getItemSummary } from '../../utils/api'
import { isAuthenticated } from '../../utils/auth'
import { Link } from "react-router-dom";

export const ItemSummary = () => {
  const [summary, setMessage] = useState<string> ('')
  const [error, setError] = useState<string> ('')

  useEffect(() => {
    // declare the data fetching function
    const fetchData = async () => {
      try {
        const summary = await getItemSummary()
        setMessage(summary)
      } catch (err) {
        setError(String(err))
      }
    }
    // call the function
    fetchData().catch(console.error);
  }, [])

  return (
      <div>
        <Card>
          <Title title='Item Summary' />
          <CardContent>
            {summary && (
              <p>
                Total cost: {summary}
              </p>
            )}
            {error && (
              <p>
                  Error: <code>{error}</code>
              </p>
            )}
          </CardContent>
        </Card>

        <Link to="items"><Button>Back</Button></Link>
      </div>
  )
}
