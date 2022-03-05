import Head from "next/head";

import Layout from "../components/layout";
import Jumbotron from "../components/jumbotron";
import { getAllPosts } from "../lib/api";
import { CMS_NAME } from "../lib/constants";
import ContactForm from "../components/contact-form";

export default function Blog() {
  return (
    <>
      <Layout>
        <Head>
          <title>Blog | {CMS_NAME}</title>
        </Head>
        <Jumbotron
          title="Latest stories"
          subtitle=""
          imageUrl="/img/logg.png"
        />
        <div className="mw9 center">
          <ul className="flex-ns flex-wrap mhn1-ns pa5-m justify-center">
            <SignForm />
          </ul>
        </div>
      </Layout>
    </>
  );
}

export async function getStaticProps() {
  const posts = getAllPosts();
  return {
    props: { posts },
  };
}

const SignForm = () => (
  <div className="mb4" style={{ margin: "2rem 0" }}>
    <h4 className="f3 b lh-title mb3 tc">Welcome!</h4>
    <form action="">
      <div className="flex-l mhn1-l" style={{ flexDirection: "column" }}>
        <div className="ph1-l w-100-l" style={{ width: "100%" }}>
          <fieldset>
            <input
              type="text"
              id="name"
              name="name"
              placeholder="Email"
              className=" mb2"
            />
            <label htmlFor="name">Name</label>
          </fieldset>
        </div>
        <div className="ph1-l w-100-l" style={{ width: "100%" }}>
          <fieldset>
            <input
              type="password"
              id="email"
              name="email"
              placeholder="Password"
              className=" mb2"
            />
            <label htmlFor="email">Email</label>
          </fieldset>
        </div>
      </div>

      <div className="tc">
        <button type="submit" className="btn w-100 w-auto-ns raise">
          Submit
        </button>
      </div>
    </form>
  </div>
);
