/* globals context */

import React from 'react'
import PropTypes from 'prop-types'
import Button from 'react-bootstrap/Button'
import Navbar from 'react-bootstrap/Navbar'
import Nav from 'react-bootstrap/Nav'
import NavDropdown from 'react-bootstrap/NavDropdown'
import Form from 'react-bootstrap/Form'
import FormControl from 'react-bootstrap/FormControl'
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import {
    Link
} from 'react-router-dom'
import apiUpdate from '../functions/apiUpdate'

export default function Main (props) {
    return (
        <>
            <Navbar bg="secondary" expand="lg" fixed="top" className="cabins-navbar">
                <Navbar.Brand href="#home"><img src={context.site_content.logo.url ?? null}/></Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="mr-auto">
                        <Nav.Link href="#home"><Link to="/" onClick={() => apiUpdate('home', props.contextState)}>Home</Link></Nav.Link>
                        <Nav.Link href="#link"><Link to="/usa/" onClick={() => apiUpdate('usa', props.contextState)}>USA</Link></Nav.Link>
                        <NavDropdown title="Dropdown" id="basic-nav-dropdown">
                            <NavDropdown.Item href="#action/3.1">Action</NavDropdown.Item>
                            <NavDropdown.Item href="#action/3.2">Another action</NavDropdown.Item>
                            <NavDropdown.Item href="#action/3.3">Something</NavDropdown.Item>
                            <NavDropdown.Divider />
                            <NavDropdown.Item href="#action/3.4">Separated link</NavDropdown.Item>
                        </NavDropdown>
                    </Nav>
                    <Form inline>
                        <FormControl type="text" placeholder="Search" className="mr-sm-2" />
                        <Button variant="outline-accent">Search</Button>
                    </Form>
                </Navbar.Collapse>
            </Navbar>
            <Container className="container-cabins primary">
                {props.children}
            </Container>

            <Container className="container-cabins secondary footer">
                <Row>
                    <Col>1 of 2</Col>
                    <Col>2 of 2</Col>
                </Row>
                <Row>
                    <Col>1 of 3</Col>
                    <Col>2 of 3</Col>
                    <Col>3 of 3</Col>
                </Row>
            </Container>

        </>
    )
}

Main.propTypes = {
    children: PropTypes.element,
    contextState: PropTypes.func
}
