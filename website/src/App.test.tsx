import { fireEvent, render, screen } from '@testing-library/react'
import App from './App'

describe('App', () => {
  it('renders the qmoney logo and github repo links', () => {
    render(<App />)

    expect(screen.getByRole('img', { name: /qmoney logo/i })).toBeInTheDocument()

    const githubLinks = screen.getAllByRole('link', { name: /github/i })
    expect(githubLinks).toHaveLength(2)
    githubLinks.forEach((link) => {
      expect(link).toHaveAttribute('href', 'https://github.com/runeape-sats/qmoney')
    })
  })

  it('toggles between light and dark mode from the header control', () => {
    render(<App />)

    const toggle = screen.getByRole('button', { name: /switch to dark mode/i })
    expect(document.documentElement).toHaveAttribute('data-theme', 'light')

    fireEvent.click(toggle)

    expect(document.documentElement).toHaveAttribute('data-theme', 'dark')
    expect(screen.getByRole('button', { name: /switch to light mode/i })).toBeInTheDocument()
  })

  it('surfaces intro, history, and current references from the readme', () => {
    render(<App />)

    expect(screen.getAllByText(/work-in-progress research repo for distributed private-key quantum cash/i).length).toBeGreaterThan(0)
    expect(screen.getByRole('heading', { name: /historical background/i })).toBeInTheDocument()
    expect(screen.getByText(/wiesner wrote the core idea in the late 1960s/i)).toBeInTheDocument()
    expect(screen.getByText(/these are the current architecture and research references highlighted in the readme/i)).toBeInTheDocument()
    expect(screen.getByRole('link', { name: /public vs private key qmoney/i })).toHaveAttribute(
      'href',
      'https://github.com/runeape-sats/qmoney/blob/main/docs/architecture/public-vs-private-key-qmoney.md',
    )
  })
})
