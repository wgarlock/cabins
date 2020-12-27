import React from 'react'
import PropTypes from 'prop-types'
import Button from 'react-bootstrap/Button'
import Navbar from 'react-bootstrap/Navbar'
import Nav from 'react-bootstrap/Nav'
import Form from 'react-bootstrap/Form'
import FormControl from 'react-bootstrap/FormControl'
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import {
    Link
} from 'react-router-dom'

export default function Main (props) {
    const {
        children,
        handlePage,
        siteContent
    } = props
    const links = siteContent.navigation

    return (
        <>
            <Navbar bg="secondary" expand="lg" fixed="top" className="cabins-navbar">
                <Navbar.Brand className="brand" href="#home">Resort &amp; Lodges</Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="mr-auto">
                        {links.map(element => {
                            return (
                                <Nav.Link key={element.slug} as={Link} to={element.url} data-src={element.id} data-content={element.contentType} onClick={handlePage}>{element.title}</Nav.Link>
                            )
                        })}
                    </Nav>
                    <Form inline>
                        <FormControl type="text" placeholder="Search" className="mr-sm-2" />
                        <Button variant="outline-accent">Search</Button>
                    </Form>
                </Navbar.Collapse>
            </Navbar>
            <Container className="container-cabins primary">
                {children}
            </Container>

            <Container className="container-cabins secondary footer">
                <Row>
                    <Col xs={12} sm={4}> Company </Col>
                    <Col xs={12} sm={4}>For Business</Col>
                    <Col xs={12} sm={4}>Contact</Col>
                </Row>
                <Row>
                    <Col xs={12} sm={4}>About</Col>
                    <Col xs={12} sm={4}>Business Blog</Col>
                    <Col xs={12} sm={4}>Sales</Col>
                </Row>
                <Row>
                    <Col xs={12} sm={4}>Jobs</Col>
                    <Col xs={12} sm={4}>Marketing Center</Col>
                    <Col xs={12} sm={4}>Support</Col>
                </Row>
                <Row>
                    <Col xs={12} sm={4}>Membership</Col>
                    <Col xs={12} sm={4}>List Your Property</Col>
                    <Col xs={12} sm={4}></Col>
                </Row>
                <Row>
                    <Col xs={12} sm={4}>Terms or Service</Col>
                    <Col xs={12} sm={4}></Col>
                    <Col xs={12} sm={4}></Col>
                </Row>
            </Container>

        </>
    )
}

Main.propTypes = {
    children: PropTypes.element,
    handlePage: PropTypes.func,
    siteContent: PropTypes.object
}
