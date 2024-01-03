import 'babel-polyfill'
import React from 'react'
import { render } from 'react-dom'
import App from './components/App'

const store = createStore(todoApp)

const rootElement = document.getElementById('root')
render(
  <Provider store={store}>
    <App />
  </Provider>,
  rootElement
)
