import { FaGithub } from "react-icons/fa";

export function Footer() {
  return (
    <footer className="border-t bg-background" style={{ paddingTop: '8px' }}>
      <div className="flex items-center justify-center gap-6">
        <a 
          href="https://github.com/mfaks/Housing-Economic-Analytics" 
          target="_blank"
          rel="noopener noreferrer"
          className="flex items-center"
        >
          <FaGithub className="text-2xl" style={{ marginRight: '8px', fontSize: '28px' }} />
        </a>
        <span className="text-lg font-light" style={{ fontSize: '22px' }}>
          Powered by Looker Studio, BigQuery, and DBT.
        </span>
      </div>
    </footer>
  )
}
