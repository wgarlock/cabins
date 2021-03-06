import React from 'react'
import PropTypes from 'prop-types'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import parse from 'html-react-parser'
import {
    Link,
    useRouteMatch
} from 'react-router-dom'

export default function Continent (props) {
    const {
        page,
        handlePage
    } = props

    const match = useRouteMatch()
    return (
        <div className="inner-container">
            <Row>
                <Col sm={6}>
                    <h1>{page.title}</h1>
                </Col>
            </Row>
            <Row>
                <Col sm={6}>
                    <Row>
                        {parse(page.description)}
                    </Row>
                    <Row>
                        <h3>Plan your trip to {page.title}</h3>
                        <p>Select a region using the map to your right or pick one from the drop down below.</p>
                        <br></br>
                        <Link to={`${match.url}ohio`} onClick={handlePage}>Ohio</Link>
                    </Row>
                </Col>
                <Col sm={6}>
                    <img src={page.heroImage.jpeg800}/>
                </Col>
            </Row>
        </div>
    )
}

Continent.propTypes = {
    page: PropTypes.object.isRequired,
    handlePage: PropTypes.func.isRequired
}
