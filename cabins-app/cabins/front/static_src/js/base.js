/* globals context */

import React, { useState } from 'react'
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

const baseContext = context

function App () {
    const [stateContext, setContext] = useState(baseContext)
    console.log(stateContext)
    return (
        <Router>
            <Main contextState={setContext}>
                <Switch>
                    <Route path="/:continent/:state/:region/:listing">
                        <Listing />
                    </Route>
                    <Route path="/:continent/:state/:region">
                        <Region />
                    </Route>
                    <Route path="/:continent/:state">
                        <State />
                    </Route>
                    <Route path="/:continent">
                        <Continent />
                    </Route>
                    <Route path="/">
                        <Home />
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
