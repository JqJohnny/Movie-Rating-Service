"""Add movie details from TMDB

Revision ID: 871f971bc7d1
Revises: a84346ef40a8
Create Date: 2024-10-01 12:34:22.119704

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '871f971bc7d1'
down_revision = 'a84346ef40a8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('movies', schema=None) as batch_op:
        batch_op.add_column(sa.Column('vote_average', sa.Float(), nullable=True))
        batch_op.alter_column('poster_path',
               existing_type=sa.VARCHAR(length=255),
               type_=sa.String(length=500),
               existing_nullable=True)
        batch_op.alter_column('release_date',
               existing_type=sa.VARCHAR(length=50),
               type_=sa.String(length=100),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('movies', schema=None) as batch_op:
        batch_op.alter_column('release_date',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=50),
               existing_nullable=True)
        batch_op.alter_column('poster_path',
               existing_type=sa.String(length=500),
               type_=sa.VARCHAR(length=255),
               existing_nullable=True)
        batch_op.drop_column('vote_average')

    # ### end Alembic commands ###
