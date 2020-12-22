/* globals context */
import React from 'react'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import parse from 'html-react-parser'
import {
    Link,
    useRouteMatch
} from 'react-router-dom'

export default function Continent () {
    const match = useRouteMatch()
    return (
        <>
            <Row>
                <Col sm={6}>
                    <h1>{context.page.title}</h1>
                </Col>
            </Row>
            <Row>
                <Col sm={6}>
                    <Row>
                        {parse(context.page.description)}
                    </Row>
                    <Row>
                        <h3>Plan your trip to {context.page.title}</h3>
                        <p>Select a region using the map to your right or pick one from the drop down below.</p>
                        <br></br>
                        <Link to={`${match.url}ohio`}>Ohio</Link>
                    </Row>
                </Col>
                <Col sm={6}>
                    <img src={context.page.hero_image.jpeg_800_url}/>
                </Col>
            </Row>
        </>
    )
}
