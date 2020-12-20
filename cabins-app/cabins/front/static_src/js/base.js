import React from 'react'
import ReactDOM from 'react-dom'
import Main from './components/main'
import Home from './views/home'

function App () {
    return (
        <Main>
            <Home/>
        </Main>
    )
}

ReactDOM.render(
    <App />,
    document.getElementById('root')
)
