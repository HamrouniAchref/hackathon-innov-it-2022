import Link from "next/link";
import PostBlock from "./post-block";

export default function Blog4Home({ posts }) {
  return (
    <div className="bg-off-white pv4">
      <div className="ph3 mw7 center">
        <h2 className="f2 b lh-title mb3">Dernières histoires</h2>
        <div className="w-100 flex-ns mhn1-ns flex-wrap mb3">
          {posts.map((p) => (
            <div key={p.title} className="ph1-ns w-50-ns flex">
              <PostBlock
                title={p.title}
                description={p.description}
                date={p.date}
                slug={p.slug}
              />
            </div>
          ))}
        </div>
        <div className="tc">
          <Link href="/marche">
            <a className="btn raise">Lire la suite</a>
          </Link>
        </div>
      </div>
    </div>
  );
}
