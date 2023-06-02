"""Staging migration to match standard

Revision ID: b0cbeeb30c9b
Revises: 
Create Date: 2023-05-19 10:52:34.529822

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "b0cbeeb30c9b"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    from sqlalchemy.schema import Sequence, CreateSequence

    op.execute(CreateSequence(Sequence("Predictions_id_seq")))
    op.create_table(
        "Predictions",
        sa.Column(
            "id",
            sa.Integer(),
            server_default=sa.text("nextval('\"Predictions_id_seq\"'::regclass)"),
            nullable=False,
        ),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("url", sa.String(), nullable=True),
        sa.Column("agency", sa.String(), nullable=True),
        sa.Column("numDocs", sa.Integer(), nullable=True),
        sa.Column("solNum", sa.String(), nullable=False),
        sa.Column("noticeType", sa.String(), nullable=False),
        sa.Column("date", sa.DateTime(), nullable=True),
        sa.Column("office", sa.String(), nullable=True),
        sa.Column("na_flag", sa.Boolean(), nullable=True),
        sa.Column(
            "eitLikelihood", postgresql.JSONB(astext_type=sa.Text()), nullable=True
        ),
        sa.Column("undetermined", sa.Boolean(), nullable=True),
        sa.Column("action", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column("actionStatus", sa.String(), nullable=True),
        sa.Column("actionDate", sa.DateTime(), nullable=True),
        sa.Column("history", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column(
            "contactInfo", postgresql.JSONB(astext_type=sa.Text()), nullable=True
        ),
        sa.Column(
            "parseStatus", postgresql.JSONB(astext_type=sa.Text()), nullable=True
        ),
        sa.Column(
            "predictions", postgresql.JSONB(astext_type=sa.Text()), nullable=True
        ),
        sa.Column("reviewRec", sa.String(), nullable=True),
        sa.Column("searchText", sa.String(), nullable=True),
        sa.Column("createdAt", sa.DateTime(), nullable=False),
        sa.Column("updatedAt", sa.DateTime(), nullable=True),
        sa.Column(
            "active", sa.Boolean(), server_default=sa.text("true"), nullable=True
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("solNum"),
    )

    op.execute(CreateSequence(Sequence("Surveys_id_seq")))
    op.create_table(
        "Surveys",
        sa.Column(
            "id",
            sa.Integer(),
            server_default=sa.text("nextval('\"Surveys_id_seq\"'::regclass)"),
            nullable=False,
        ),
        sa.Column("question", sa.Text(), nullable=True),
        sa.Column("choices", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column("section", sa.String(length=2000), nullable=True),
        sa.Column("type", sa.String(length=2000), nullable=True),
        sa.Column("answer", sa.Text(), nullable=True),
        sa.Column("note", sa.Text(), nullable=True),
        sa.Column(
            "choicesNote", postgresql.JSONB(astext_type=sa.Text()), nullable=True
        ),
        sa.Column("createdAt", sa.DateTime(), nullable=False),
        sa.Column("updatedAt", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )

    op.execute(CreateSequence(Sequence("agency_alias_id_seq")))
    op.create_table(
        "agency_alias",
        sa.Column(
            "id",
            sa.Integer(),
            server_default=sa.text("nextval('agency_alias_id_seq'::regclass)"),
            nullable=False,
        ),
        sa.Column("agency_id", sa.Integer(), nullable=False),
        sa.Column("alias", sa.String(), nullable=True),
        sa.Column("createdAt", sa.DateTime(), nullable=True),
        sa.Column("updatedAt", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )

    op.execute(CreateSequence(Sequence("model_id_seq")))
    op.create_table(
        "model",
        sa.Column(
            "id",
            sa.Integer(),
            server_default=sa.text("nextval('model_id_seq'::regclass)"),
            nullable=False,
        ),
        sa.Column("results", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column("params", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column("score", sa.Float(precision=53), nullable=True),
        sa.Column("create_date", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )

    op.execute(CreateSequence(Sequence("notice_type_id_seq")))
    op.create_table(
        "notice_type",
        sa.Column(
            "id",
            sa.Integer(),
            server_default=sa.text("nextval('notice_type_id_seq'::regclass)"),
            nullable=False,
        ),
        sa.Column("notice_type", sa.String(length=50), nullable=True),
        sa.Column("createdAt", sa.DateTime(), nullable=False),
        sa.Column("updatedAt", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_notice_type_notice_type"), "notice_type", ["notice_type"], unique=False
    )
    op.create_table(
        "survey_backup",
        sa.Column("id", sa.Integer(), nullable=True, primary_key=True),
        sa.Column("question", sa.Text(), nullable=True),
        sa.Column("choices", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column("section", sa.String(length=2000), nullable=True),
        sa.Column("type", sa.String(length=2000), nullable=True),
        sa.Column("answer", sa.Text(), nullable=True),
        sa.Column("note", sa.Text(), nullable=True),
        sa.Column(
            "choicesNote", postgresql.JSONB(astext_type=sa.Text()), nullable=True
        ),
        sa.Column("createdAt", sa.DateTime(), nullable=True),
        sa.Column("updatedAt", sa.DateTime(), nullable=True),
    )

    op.execute(CreateSequence(Sequence("survey_responses_id_seq")))
    op.create_table(
        "survey_responses",
        sa.Column(
            "id",
            sa.Integer(),
            server_default=sa.text("nextval('survey_responses_id_seq'::regclass)"),
            nullable=False,
        ),
        sa.Column("solNum", sa.String(), nullable=True),
        sa.Column("contemporary_notice_id", sa.Integer(), nullable=True),
        sa.Column(
            "response",
            postgresql.JSONB(astext_type=sa.Text()),
            server_default=sa.text("'[]'::jsonb"),
            nullable=True,
        ),
        sa.Column("maxId", sa.String(length=256), nullable=True),
        sa.Column("createdAt", sa.DateTime(), nullable=False),
        sa.Column("updatedAt", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_index(
        op.f("ix_survey_responses_solNum"), "survey_responses", ["solNum"], unique=False
    )

    op.execute(CreateSequence(Sequence("survey_responses_archive_id_seq")))
    op.create_table(
        "survey_responses_archive",
        sa.Column(
            "id",
            sa.Integer(),
            server_default=sa.text(
                "nextval('survey_responses_archive_id_seq'::regclass)"
            ),
            nullable=False,
        ),
        sa.Column("solNum", sa.String(), nullable=True),
        sa.Column("contemporary_notice_id", sa.Integer(), nullable=True),
        sa.Column(
            "response",
            postgresql.JSONB(astext_type=sa.Text()),
            server_default=sa.text("'[]'::jsonb"),
            nullable=True,
        ),
        sa.Column("maxId", sa.String(length=256), nullable=True),
        sa.Column(
            "original_created_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.Column("createdAt", sa.DateTime(), nullable=False),
        sa.Column("updatedAt", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "winston_logs",
        sa.Column("timestamp", sa.DateTime(timezone=True), nullable=True),
        sa.Column("level", sa.String(length=255), nullable=True),
        sa.Column("message", sa.Text(), nullable=True),
        sa.Column("meta", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    )

    op.execute(CreateSequence(Sequence("attachment_id_seq")))
    op.create_table(
        "attachment",
        sa.Column(
            "id",
            sa.Integer(),
            server_default=sa.text("nextval('attachment_id_seq'::regclass)"),
            nullable=False,
        ),
        sa.Column("notice_id", sa.Integer(), nullable=True),
        sa.Column("notice_type_id", sa.Integer(), nullable=True),
        sa.Column("machine_readable", sa.Boolean(), nullable=True),
        sa.Column("attachment_text", sa.Text(), nullable=True),
        sa.Column("prediction", sa.Integer(), nullable=True),
        sa.Column("decision_boundary", sa.Float(precision=53), nullable=True),
        sa.Column("validation", sa.Integer(), nullable=True),
        sa.Column("attachment_url", sa.Text(), nullable=True),
        sa.Column("trained", sa.Boolean(), nullable=True),
        sa.Column("createdAt", sa.DateTime(), nullable=False),
        sa.Column("updatedAt", sa.DateTime(), nullable=True),
        sa.Column("filename", sa.Text(), nullable=False),
        sa.Column("solicitation_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["notice_type_id"],
            ["notice_type.id"],
        ),
        sa.ForeignKeyConstraint(
            ["solicitation_id"],
            ["solicitations.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )

    op.execute(CreateSequence(Sequence("notice_id_seq")))
    op.create_table(
        "notice",
        sa.Column(
            "id",
            sa.Integer(),
            server_default=sa.text("nextval('notice_id_seq'::regclass)"),
            nullable=False,
        ),
        sa.Column("notice_type_id", sa.Integer(), nullable=True),
        sa.Column("solicitation_number", sa.String(length=150), nullable=True),
        sa.Column("agency", sa.String(length=150), nullable=True),
        sa.Column("date", sa.DateTime(), nullable=True),
        sa.Column(
            "notice_data", postgresql.JSONB(astext_type=sa.Text()), nullable=True
        ),
        sa.Column("compliant", sa.Integer(), nullable=True),
        sa.Column("feedback", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column("history", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column("action", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column("createdAt", sa.DateTime(), nullable=False),
        sa.Column("updatedAt", sa.DateTime(), nullable=True),
        sa.Column("na_flag", sa.Boolean(), nullable=True),
        sa.ForeignKeyConstraint(
            ["notice_type_id"],
            ["notice_type.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_notice_solicitation_number"),
        "notice",
        ["solicitation_number"],
        unique=False,
    )
    op.alter_column(
        "Agencies",
        "updatedAt",
        existing_type=postgresql.TIMESTAMP(timezone=True),
        nullable=True,
    )
    op.add_column("Users", sa.Column("maxId", sa.String(length=256), nullable=True))
    op.alter_column(
        "Users",
        "updatedAt",
        existing_type=postgresql.TIMESTAMP(timezone=True),
        nullable=True,
    )
    op.create_unique_constraint(None, "solicitations", ["solNum"])

    # Solcitations
    op.create_unique_constraint(None, "solicitations", ["solNum"])
    op.alter_column("solicitations", "history", server_default=sa.text("'[]'::jsonb"))
    op.alter_column("solicitations", "action", server_default=sa.text("'[]'::jsonb"))
    op.alter_column(
        "solicitations",
        "predictions",
        server_default=sa.text('\'{"value": "red", "history": []}\'::jsonb'),
    )
    op.alter_column("solicitations", "compliant", server_default=sa.text("0"))
    op.alter_column("solicitations", "active", server_default=sa.text("true"))
    op.alter_column("solicitations", "na_flag", server_default=sa.text("false"))
    op.alter_column("solicitations", "updatedAt", nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "solicitations", type_="unique")
    op.alter_column(
        "Users",
        "updatedAt",
        existing_type=postgresql.TIMESTAMP(timezone=True),
        nullable=False,
    )
    op.drop_column("Users", "maxId")
    op.alter_column(
        "Agencies",
        "updatedAt",
        existing_type=postgresql.TIMESTAMP(timezone=True),
        nullable=False,
    )
    op.drop_index(op.f("ix_notice_solicitation_number"), table_name="notice")
    op.drop_table("notice")
    op.drop_table("attachment")
    op.drop_table("winston_logs")
    op.drop_table("survey_responses_archive")
    op.drop_index(op.f("ix_survey_responses_solNum"), table_name="survey_responses")
    op.drop_table("survey_responses")
    op.drop_table("survey_backup")
    op.drop_index(op.f("ix_notice_type_notice_type"), table_name="notice_type")
    op.drop_table("notice_type")
    op.drop_table("model")
    op.drop_table("agency_alias")
    op.drop_table("Surveys")
    op.drop_table("Predictions")
    # ### end Alembic commands ###
