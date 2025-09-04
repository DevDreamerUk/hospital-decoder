from yoyo import step

steps = [
    step(
        """
         CREATE SCHEMA IF NOT EXISTS social;
        """
    ),

    step(
        """
        CREATE TABLE IF NOT EXISTS general.emz_records 
        (
            id                             SERIAL PRIMARY KEY,
            report_year                    INT,
            report_month                   INT,
            emz_type                       TEXT,
            emz_id                         TEXT,
            submitted_to_esoz              TEXT,
            executor_position              TEXT,
            executor_name                  TEXT,
            service_location               TEXT,
            referral_type                  TEXT,
            referral_org_edrpou            TEXT,
            referral_doctor_position       TEXT,
            episode_id                     TEXT,
            episode_type                   TEXT,
            episode_start                  TIMESTAMP,
            dz_start                       TIMESTAMP,
            episode_end                    TIMESTAMP,
            treatment_duration_days        INT,
            main_diagnosis                 TEXT,
            main_diagnosis_validity_status TEXT,
            main_diagnosis_clinical_status TEXT,
            additional_diagnoses           TEXT,
            disproved_additional_diagnoses TEXT,
            interventions                  TEXT,
            interaction_class              TEXT,
            priority                       TEXT,
            interaction_type               TEXT,
            hospitalization_reason         TEXT,
            treatment_result               TEXT,
            patient_unique_code            TEXT,
            patient_has_declaration        TEXT,
            patient_gender                 TEXT,
            patient_weight_grams           INT,
            patient_age_days               INT,
            patient_age_years              INT,
            adsg                           TEXT,
            service_package                TEXT,
            service_number                 TEXT,
            tariff                         NUMERIC(12, 2),
            payment_amount                 NUMERIC(12, 2),
            included_in_statistics         TEXT,
            included_in_report             TEXT,
            error_comment                  TEXT,
            error_details                  TEXT,
            mismatch_details               TEXT,
            grouping_conflicts             TEXT,
            nszu_package_review_details    TEXT,
            additional_comments            TEXT,
            nszu_review_date               DATE
        );

        """,

    )
]