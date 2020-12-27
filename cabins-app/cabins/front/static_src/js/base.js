/* globals context */

import React, { useState, useEffect, useCallback } from 'react'
import ReactDOM from 'react-dom'
import Main from './components/main'
import Home from './views/home'
import Continent from './views/continent'
import State from './views/state'
import Region from './views/region'
import Listing from './views/listing'
import {
    BrowserRouter as Router,
    Switch,
    Route
} from 'react-router-dom'

import request from './functions/apiUpdate'

function App () {
    const [page, setPage] = useState(context.page)
    const siteContent = context.site_content
    const handlePage = useCallback((e) => {
        const link = e.target
        request({ endpoint: link, headers: { 'Content-Type': 'application/json' } }).then(res => {
            const data = JSON.parse(res)
            setPage(data.data[`get${link.getAttribute('data-content')}ById`])
        }
        ).catch(err => {
            console.log(err)
        })
    }, [setPage])

    useEffect(() => {
    }, [page])

    return (
        <Router>
            <Main siteContent={siteContent} handlePage={handlePage}>
                <Switch>
                    <Route path="/:continent/:state/:region/:listing">
                        <Listing handlePage = {handlePage} page={page}/>
                    </Route>
                    <Route path="/:continent/:state/:region">
                        <Region handlePage = {handlePage} page={page}/>
                    </Route>
                    <Route path="/:continent/:state">
                        <State handlePage = {handlePage} page={page}/>
                    </Route>
                    <Route path="/:continent">
                        <Continent handlePage = {handlePage} page={page}/>
                    </Route>
                    <Route path="/">
                        <Home handlePage = {handlePage} page={page}/>
                    </Route>
                </Switch>
            </Main>
        </Router>
    )
}

ReactDOM.render(
    <App />,
    document.getElementById('root')
)
