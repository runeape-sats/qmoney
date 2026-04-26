import { fireEvent, render, screen, within } from '@testing-library/react'
import App from './App'

describe('App', () => {
  it('renders the qmoney logo and github repo link inside the expandable header panel', () => {
    render(<App />)

    expect(screen.getByRole('img', { name: /qmoney logo/i })).toBeInTheDocument()

    const menuButton = screen.getByRole('button', { name: /open site menu/i })
    fireEvent.click(menuButton)

    const githubLink = within(screen.getByRole('region', { name: /site navigation panel/i })).getByRole('link', {
      name: /github/i,
    })

    expect(githubLink).toHaveAttribute('href', 'https://github.com/runeape-sats/qmoney')
  })

  it('toggles between light and dark mode from the expandable header panel', () => {
    render(<App />)

    fireEvent.click(screen.getByRole('button', { name: /open site menu/i }))

    const toggle = within(screen.getByRole('region', { name: /site navigation panel/i })).getByRole('button', {
      name: /switch to dark mode/i,
    })
    expect(document.documentElement).toHaveAttribute('data-theme', 'light')

    fireEvent.click(toggle)

    expect(document.documentElement).toHaveAttribute('data-theme', 'dark')
    expect(
      within(screen.getByRole('region', { name: /site navigation panel/i })).getByRole('button', {
        name: /switch to light mode/i,
      }),
    ).toBeInTheDocument()
  })

  it('toggles the expandable site menu and collapses it after navigation', () => {
    render(<App />)

    const menuButton = screen.getByRole('button', { name: /open site menu/i })
    const siteMenu = document.getElementById('site-navigation-panel')

    if (!siteMenu) {
      throw new Error('site navigation panel not found')
    }

    expect(menuButton).toHaveAttribute('aria-expanded', 'false')
    expect(siteMenu).toHaveAttribute('hidden')

    fireEvent.click(menuButton)

    expect(menuButton).toHaveAttribute('aria-expanded', 'true')
    expect(siteMenu).not.toHaveAttribute('hidden')

    fireEvent.click(within(siteMenu).getByRole('link', { name: /history/i }))

    expect(screen.getByRole('button', { name: /open site menu/i })).toHaveAttribute('aria-expanded', 'false')
    expect(siteMenu).toHaveAttribute('hidden')
  })

  it('surfaces intro, comparison, history, and current references from the readme', () => {
    render(<App />)

    expect(screen.getAllByText(/work-in-progress research repo for distributed private-key quantum cash/i).length).toBeGreaterThan(0)
    fireEvent.click(screen.getByRole('button', { name: /open site menu/i }))
    expect(within(screen.getByRole('region', { name: /site navigation panel/i })).getByRole('link', { name: /compare/i })).toHaveAttribute(
      'href',
      '#comparison',
    )
    expect(screen.getByRole('region', { name: /qmoney and bitcoin comparison/i })).toBeInTheDocument()
    expect(screen.getByRole('columnheader', { name: /pubkey_hidden_subspace/i })).toBeInTheDocument()
    expect(screen.getByText(/public-verification workflow, not for claiming production-grade public-key quantum money/i)).toBeInTheDocument()
    expect(screen.getByRole('heading', { name: /historical background/i })).toBeInTheDocument()
    expect(screen.getByText(/wiesner wrote the core idea in the late 1960s/i)).toBeInTheDocument()
    expect(screen.getByText(/these are the current architecture and research references highlighted in the readme/i)).toBeInTheDocument()
    expect(screen.getByRole('link', { name: /public vs private key qmoney/i })).toHaveAttribute(
      'href',
      'https://github.com/runeape-sats/qmoney/blob/main/docs/architecture/public-vs-private-key-qmoney.md',
    )
    expect(screen.getByRole('link', { name: /ekert quantum cryptography and qmoney/i })).toHaveAttribute(
      'href',
      'https://github.com/runeape-sats/qmoney/blob/main/docs/research/ekert-quantum-cryptography-and-qmoney.md',
    )
  })
})
