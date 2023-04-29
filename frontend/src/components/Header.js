import "./Header.css"
function Header(){
    return(
        <header id={'carStore'} className={'header'}>
            <a href={'carStore'} className={'head__link'}>Car Store Name</a>
            <nav className={'nav'}>
                <ul className={'list'}>
                    <li className={'list__item'}><a href={'#hero'}>About</a></li>
                    <li className={'list__item'}><a href={'#cars'}>Cars</a></li>
                    <li className={'list__item'}><a href={'#contact'}>Contact</a></li>
                </ul>
            </nav>
        </header>
    )
}

export default Header