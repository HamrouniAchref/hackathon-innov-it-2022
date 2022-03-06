import Head from "next/head";

import Layout from "../components/layout";
import Jumbotron from "../components/jumbotron";
import PostBlock from "../components/post-block";
import { getAllPosts } from "../lib/api";
import { CMS_NAME } from "../lib/constants";
import Select from "react-select";
import { useState } from "react";
import Dropzone, { useDropzone } from "react-dropzone";

export default function Blog({ posts }) {
  return (
    <>
      <Layout>
        <Head>
          <title>Blog | {CMS_NAME}</title>
        </Head>
        <Jumbotron
          title="Besoin d'une formation ?"
          subtitle="Compte sur nous"
          imageUrl="/img/formation.jpg"
        />

        <div className="mw9 center">
          <ul className="flex-ns flex-wrap mhn1-ns pa5-m justify-center">
            <FormationForm />
          </ul>
          <ul
            className="flex-ns flex-wrap mhn1-ns pa5-m justify-center"
            style={{ paddingTop: "0rem", marginTop: "0rem" }}
          >
            {posts.map((p) => (
              <div key={p.title} className="flex w-30-l w-50-m ph2-ns pv2-ns ">
                <PostBlock
                  title={p.title}
                  description={p.description}
                  date={p.date}
                  slug={p.slug}
                />
              </div>
            ))}
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

const FormationForm = () => {
  const [selectedOption, setselectedOption] = useState(null);
  return (
    <div className="mb0">
      <h4 className="f3 b lh-title mb3 tc">
        Merci de remplir ce court formulaire
      </h4>
      <form
        onSubmit={(e) => {
          e.preventDefault();
        }}
      >
        <div className="flex-l mhn1-l">
          <div className="ph1-l w-50-l">
            <fieldset>
              <input
                type="text"
                id="name"
                name="name"
                placeholder="Nom"
                className="w-100 mb2"
              />
              <label htmlFor="name">Name</label>
            </fieldset>
          </div>
          <div className="ph1-l w-50-l">
            <fieldset>
              <input
                type="email"
                id="email"
                name="email"
                placeholder="Prénom"
                className="w-100 mb2"
              />
              <label htmlFor="email">Email</label>
            </fieldset>
          </div>
        </div>
        <fieldset>
          <input
            type="email"
            id="email"
            name="email"
            placeholder="Email"
            className="w-100 mb2"
          />
          <label htmlFor="email">Email</label>
        </fieldset>
        <fieldset className="w-100 mb2">
          <Select
            value={selectedOption}
            placeholder="Selectionner votre domaine"
            onChange={(selectedOption) => {
              setselectedOption(selectedOption);
            }}
            options={[
              { value: "Recyclage", label: "Recyclage" },
              { value: "Reparation", label: "Reparation" },
              { value: "Energie Renouvale", label: "Energie Renouvale" },
            ]}
            styles={{
              placeholder: (provided) => ({
                ...provided,
                color: "black",
                background: "#EBE7E6",
              }),
              option: (provided, state) => ({
                ...provided,
                background: "#EBE7E6",
                zIndex: 999,
              }),
            }}
          />
        </fieldset>
        <div
          className="w-100 mb2 center"
          style={{
            background: "#EBE7E6",
            opacity: "0.7",
            border: "1px dashed black",
            width: "50%",
          }}
        >
          <Basic />
        </div>
        <textarea
          id="message"
          name="message"
          placeholder="Commentaire"
          rows="8"
          cols="80"
          className="w-100"
        />
        <label htmlFor="message">Votre commentaire...</label>

        <div className="tc">
          <button type="submit" className="btn w-100 w-auto-ns raise">
            Soumettre
          </button>
        </div>
      </form>
    </div>
  );
};

export function Basic({ bool }) {
  const { acceptedFiles, getRootProps, getInputProps } = useDropzone();

  const files = acceptedFiles.map((file) => (
    <li key={file.path}>
      {file.path} - {file.size} bytes
    </li>
  ));

  return (
    <section style={{ cursor: "pointer" }}>
      <div {...getRootProps({ className: "dropzone" })}>
        <input {...getInputProps()} />
        <p style={{ fontSize: "0.75rem", color: "black" }}>
          Faites glisser et déposez des fichiers ici, ou cliquez pour
          sélectionner des fichiers
        </p>
      </div>
      <aside>
        <span style={{ fontSize: "0.6rem" }}>
          {" "}
          {bool ? "Photo" : "Diplome / CV"}
        </span>
        <ul>{files}</ul>
      </aside>
    </section>
  );
}
